import http from 'k6/http';
import { check, sleep } from 'k6';

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

const body = JSON.stringify({
    title: 'foo',
    body: 'bar',
    userId: 1,
});

export default function (data) {
    const url = 'https://jsonplaceholder.typicode.com/posts';
    const params = {
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
    };

    const res = http.post(url, body, params);
    check(res, { 'status is 201': (r) => r.status === 201 });
}