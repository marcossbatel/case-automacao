import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
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

export default function (data) {
    const url = 'https://jsonplaceholder.typicode.com/posts';
    const res = http.get(url);
    check(res, { 'status is 200': (r) => r.status === 200 });
}