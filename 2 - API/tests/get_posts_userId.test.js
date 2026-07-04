import { describe, test, expect, beforeAll } from 'vitest';
import axios from 'axios';

const BASE_URL = 'https://jsonplaceholder.typicode.com';
const USER_ID = 1;

let response;
let data;

describe('GET /posts?userId=1 - Listar posts', () => {
    beforeAll(async () => {
        response = await axios.get(`${BASE_URL}/posts`, {
            params: { userId: USER_ID }
        });
        data = response.data;
    });

    test('Deve retornar status code 200', () => {
        expect(response.status).toBe(200);
    });

    test('Deve retornar uma lista (array)', () => {
        expect(Array.isArray(data)).toBe(true);
    });

    test('A lista não deve estar vazia', () => {
        expect(data.length).toBeGreaterThan(0);
    });

    test('Deve retornar exatamente 10 posts para userId=1', () => {
        expect(data.length).toBe(10);
    });

    test('Todos os posts devem pertencer ao userId=1', () => {
        data.forEach(post => {
            expect(post.userId).toBe(USER_ID);
        });
    });

    test('O campo "id" de todos os posts devem ser do tipo number', () => {
        data.forEach(post => {
            expect(typeof post.id).toBe('number');
        });
    });

    test('O campo "title" deve ser do tipo string', () => {
        expect(typeof data[0].title).toBe('string');
    });

    test('O campo "body" deve ser do tipo string', () => {
        expect(typeof data[0].body).toBe('string');
    });

    test('O campo "userId" deve ser do tipo number', () => {
        expect(typeof data[0].userId).toBe('number');
    });

    test('O campo "title" não deve estar vazio', () => {
        data.forEach(post => {
            expect(post.title.length).toBeGreaterThan(0);
        });
    });

    test('O campo "body" não deve estar vazio', () => {
        expect(data[0].body.length).toBeGreaterThan(0);
    });

    test('Todos os posts devem ter os campos obrigatórios', () => {
        const camposObrigatorios = ['id', 'title', 'body', 'userId'];

        data.forEach(post => {
            camposObrigatorios.forEach(field => {
                expect(post).toHaveProperty(field);
            });
        });
    });

});

describe('GET /posts?userId=X - Cenários de Borda', () => {
    test('Deve retornar lista vazia para usuário inexistente', async () => {
        const response = await axios.get(`${BASE_URL}/posts`, {
            params: { userId: 99999 }
        });

        expect(response.status).toBe(200);
        expect(Array.isArray(response.data)).toBe(true);
        expect(response.data.length).toBe(0);
    });

    test('Deve processar requisição com userId=0', async () => {
        const response = await axios.get(`${BASE_URL}/posts`, {
            params: { userId: 0 }
        });

        expect(response.status).toBe(200);
        expect(Array.isArray(response.data)).toBe(true);
    });

    test('Deve processar requisição com userId negativo', async () => {
        const response = await axios.get(`${BASE_URL}/posts`, {
            params: { userId: -1 }
        });

        expect(response.status).toBe(200);
        expect(Array.isArray(response.data)).toBe(true);
    });

    test('Deve retornar posts do usuário 2 corretamente', async () => {
        const response = await axios.get(`${BASE_URL}/posts`, {
            params: { userId: 2 }
        });

        expect(response.status).toBe(200);
        expect(response.data.length).toBe(10);
        response.data.forEach(post => {
            expect(post.userId).toBe(2);
        });
    });

    test('Deve retornar posts do usuário 10 corretamente', async () => {
        const response = await axios.get(`${BASE_URL}/posts`, {
            params: { userId: 10 }
        });

        expect(response.status).toBe(200);
        expect(response.data.length).toBe(10);
        response.data.forEach(post => {
            expect(post.userId).toBe(10);
        });
    });

    test('Deve processar múltiplos parâmetros corretamente', async () => {
        const response = await axios.get(`${BASE_URL}/posts`, {
            params: { userId: 1, id: 1 }
        });

        expect(response.status).toBe(200);
        expect(Array.isArray(response.data)).toBe(true);
    });
});
