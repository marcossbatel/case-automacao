import { describe, test, expect, beforeAll } from 'vitest';
import axios from 'axios';

const BASE_URL = 'https://jsonplaceholder.typicode.com';
let response;
let data;

describe('GET /posts - Listar todos os posts', () => {
    beforeAll(async () => {
        response = await axios.get(`${BASE_URL}/posts`);
        data = response.data;
    });

    test('Deve retornar status code 200', () => {
        expect(response.status).toBe(200);
    });

    test('A resposta é um objeto JSON', () => {
        expect(typeof data).toBe('object');
    });

    test('O array não deve estar vazio', () => {
        expect(data.length).toBeGreaterThan(0);
    });

    test('Todos os items possuem a estrutura correta', () => {
        data.forEach((post) => {
            expect(post).to.have.property("userId");
            expect(post).to.have.property("id");
            expect(post).to.have.property("title");
            expect(post).to.have.property("body");
            expect(post.userId).to.not.be.null;
            expect(post.id).to.not.be.null;
            expect(post.title).to.not.be.empty;
            expect(post.body).to.not.be.empty;
        })
    });

    test('O tipo de todos os itens está correto', () => {
        data.forEach((post) => {
            expect(post.userId).to.be.a("number");
            expect(post.id).to.be.a("number");
            expect(post.title).to.be.a("string");
            expect(post.body).to.be.a("string");
        })
    });
});
