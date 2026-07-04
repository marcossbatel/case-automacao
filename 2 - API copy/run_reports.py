from __future__ import annotations

import html
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORTS_DIR = ROOT / "reports"
REPORTS_DIR.mkdir(exist_ok=True)


def run_command(command: list[str], cwd: Path) -> tuple[int, str, str]:
    completed = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    return completed.returncode, completed.stdout, completed.stderr


python_result = None
vitest_result = None

python_command = [sys.executable, "-m", "pytest", "-q", "--html", str(REPORTS_DIR / "python-report.html"), "tests/python"]
npm_executable = shutil.which("npm.cmd") or shutil.which("npm") or "npm"
vitest_command = [npm_executable, "run", "test:vitest"]

python_code, python_stdout, python_stderr = run_command(python_command, ROOT)
python_result = {
    "code": python_code,
    "stdout": python_stdout,
    "stderr": python_stderr,
}

vitest_code, vitest_stdout, vitest_stderr = run_command(vitest_command, ROOT)
vitest_result = {
    "code": vitest_code,
    "stdout": vitest_stdout,
    "stderr": vitest_stderr,
}

summary = {
    "python": python_code == 0,
    "vitest": vitest_code == 0,
}

html_report_path = REPORTS_DIR / "execution-report.html"
html_report_path.write_text(
    """<!DOCTYPE html>
<html lang=\"pt-BR\">
  <head>
    <meta charset=\"utf-8\" />
    <title>Relatório de execução dos testes de API</title>
    <style>
      body {{ font-family: Arial, sans-serif; margin: 2rem; line-height: 1.5; }}
      h1, h2 {{ color: #1f2937; }}
      .success {{ color: #047857; }}
      .failure {{ color: #b91c1c; }}
      .card {{ border: 1px solid #d1d5db; border-radius: 8px; padding: 1rem; margin-bottom: 1rem; }}
      pre {{ background: #f3f4f6; padding: 1rem; border-radius: 6px; overflow-x: auto; }}
      a {{ color: #2563eb; }}
    </style>
  </head>
  <body>
    <h1>Relatório de execução dos testes de API</h1>
    <p>Gerado em: {timestamp}</p>
    <div class=\"card\">
      <h2>Resumo</h2>
      <p><strong>Python:</strong> <span class=\"{python_class}\">{python_status}</span></p>
      <p><strong>Vitest:</strong> <span class=\"{vitest_class}\">{vitest_status}</span></p>
      <p><strong>Relatório Python:</strong> <a href=\"python-report.html\">python-report.html</a></p>
    </div>
    <div class=\"card\">
      <h2>Execução Python</h2>
      <p><strong>Comando:</strong> {python_command}</p>
      <pre>{python_stdout}</pre>
      <pre>{python_stderr}</pre>
    </div>
    <div class=\"card\">
      <h2>Execução Vitest</h2>
      <p><strong>Comando:</strong> {vitest_command}</p>
      <pre>{vitest_stdout}</pre>
      <pre>{vitest_stderr}</pre>
    </div>
  </body>
</html>
""".format(
        timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        python_class="success" if summary["python"] else "failure",
        python_status="PASSOU" if summary["python"] else "FALHOU",
        vitest_class="success" if summary["vitest"] else "failure",
        vitest_status="PASSOU" if summary["vitest"] else "FALHOU",
        python_command=html.escape(" ".join(python_command)),
        python_stdout=html.escape(python_result["stdout"]),
        python_stderr=html.escape(python_result["stderr"]),
        vitest_command=html.escape(" ".join(vitest_command)),
        vitest_stdout=html.escape(vitest_result["stdout"]),
        vitest_stderr=html.escape(vitest_result["stderr"]),
    ),
    encoding="utf-8",
)

print(f"Relatório HTML gerado em: {html_report_path}")
