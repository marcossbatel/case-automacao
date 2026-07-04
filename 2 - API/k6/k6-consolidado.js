import http from 'k6/http';
import { check, group, sleep } from 'k6';
import { Trend } from 'k6/metrics';

export const options = {
    // iterations: 1,
    stages: [
        { duration: '5s', target: 50 },
        { duration: '1s', target: 100 },
        { duration: '1s', target: 50 },
        { duration: '13s', target: 50 },
        { duration: '10s', target: 0 }
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(99)<500'],
    },
};

const base_url = 'https://jsonplaceholder.typicode.com';
const body = JSON.stringify({
    title: 'foo',
    body: 'bar',
    userId: 1,
});
const params = {
    headers: {
        'Content-type': 'application/json; charset=UTF-8',
    },
};

const getPostsLatency = new Trend('posts');
const getPostsIdLatency = new Trend('posts_id');
const postPostsLatency = new Trend('criar_posts_id');

export default function (data) {
    const baseUrl = 'https://jsonplaceholder.typicode.com';
    let res;

    group('Consulta de Posts', function () {
      res = http.get(`${baseUrl}/posts`);
      getPostsLatency.add(res.timings.duration);
      check(res, { 'status is 200': (r) => r.status === 200 });
    });

    group('Consulta de Posts por ID', function () {
      res = http.get(`${baseUrl}/posts/1`);
      getPostsIdLatency.add(res.timings.duration);
      check(res, { 'status is 200': (r) => r.status === 200 });
    });

    group('Cadastro de Posts', function () {
      res = http.post(`${baseUrl}/posts`, body, params);
      postPostsLatency.add(res.timings.duration);
      check(res, { 'status is 201': (r) => r.status === 201 });
    });

}
