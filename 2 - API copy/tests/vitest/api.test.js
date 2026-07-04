import { describe, expect, it } from 'vitest';

const BASE_URL = 'https://jsonplaceholder.typicode.com';

async function request(method, path, payload, headers = {}) {
  const options = {
    method,
    headers,
  };

  if (payload !== undefined) {
    options.body = JSON.stringify(payload);
  }

  const response = await fetch(`${BASE_URL}${path}`, options);
  const body = await response.json();
  return { status: response.status, body };
}

describe('API de posts', () => {
  it('deve retornar posts de um usuário específico', async () => {
    const { status, body } = await request('GET', '/posts?userId=1');

    expect(status).toBe(200);
    expect(Array.isArray(body)).toBe(true);
    expect(body.length).toBeGreaterThan(0);
    expect(body.every((item) => item.userId === 1)).toBe(true);
    expect(body.every((item) => ['id', 'title', 'body', 'userId'].every((key) => key in item))).toBe(true);
  });

  it('deve criar um novo post com sucesso', async () => {
    const payload = {
      title: 'foo',
      body: 'bar',
      userId: 1,
    };

    const { status, body } = await request('POST', '/posts', payload, {
      'Content-Type': 'application/json; charset=UTF-8',
    });

    expect(status).toBe(201);
    expect(body).toEqual(
      expect.objectContaining({
        title: 'foo',
        body: 'bar',
        userId: 1,
      }),
    );
    expect(body.id).toBeDefined();
  });

  it('deve retornar um post específico por id', async () => {
    const { status, body } = await request('GET', '/posts/1');

    expect(status).toBe(200);
    expect(body).toEqual(
      expect.objectContaining({
        id: 1,
        userId: 1,
      }),
    );
    expect(['id', 'title', 'body', 'userId'].every((key) => key in body)).toBe(true);
  });

  it('deve retornar uma lista vazia para um usuário sem posts', async () => {
    const { status, body } = await request('GET', '/posts?userId=999');

    expect(status).toBe(200);
    expect(body).toEqual([]);
  });

  it('deve retornar 404 e objeto vazio para um post inexistente', async () => {
    const response = await fetch(`${BASE_URL}/posts/999`);
    const body = await response.json();

    expect(response.status).toBe(404);
    expect(body).toEqual({});
  });
});
