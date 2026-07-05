import { describe, test, expect, beforeAll } from 'vitest';
import axios from 'axios';

const BASE_URL = 'https://jsonplaceholder.typicode.com';
const POST_DATA = {
    title: 'foo',
    body: 'bar',
    userId: 1
};

let response;
let data;

describe('POST /posts - Criar novo post', () => {
    beforeAll(async () => {
        response = await axios.post(`${BASE_URL}/posts`, POST_DATA, {
            headers: {
                'Content-type': 'application/json; charset=UTF-8'
            }
        });
        data = response.data;
    });

    test('Status deve ser 201 (Created)', () => {
        expect(response.status).toBe(201);
    });

    test('A resposta é um objeto JSON', () => {
        expect(data).to.be.an("object");
    });

    test('A resposta contém um ID e ele é do tipo número', () => {
        expect(data.id).to.exist;
        expect(data.id).to.be.a("number");
    });

    test('Os dados da resposta são iguais ao dados informados no corpo da requisição', () => {
        expect(data.title).to.equal(POST_DATA.title);
        expect(data.body).to.equal(POST_DATA.body);
        expect(data.userId).to.equal(POST_DATA.userId);
    });

    test('A resposta possui todos os campos', () => {
        expect(data).to.have.property("id");
        expect(data).to.have.property("title");
        expect(data).to.have.property("body");
        expect(data).to.have.property("userId");
    });

    test('Os tipos dos campos são corretos', () => {
        expect(typeof data.id).toBe('number');
        expect(typeof data.title).toBe('string');
        expect(typeof data.body).toBe('string');
        expect(typeof data.userId).toBe('number');
    });
});
