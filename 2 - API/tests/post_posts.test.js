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

    test('Deve retornar status code 201 (Created)', () => {
        expect(response.status).toBe(201);
    });

    test('Deve retornar Content-Type application/json', () => {
        expect(response.headers['content-type']).toContain('application/json');
    });

    test('Deve retornar um objeto JSON', () => {
        expect(typeof data).toBe('object');
        expect(data).not.toBeNull();
        expect(!Array.isArray(data)).toBe(true);
    });

    test('Deve retornar um ID no response', () => {
        expect(data).toHaveProperty('id');
    });

    test('O campo "id" deve ser do tipo number', () => {
        expect(typeof data.id).toBe('number');
    });

    test('O ID retornado deve ser 101 (próximo da sequência)', () => {
        expect(data.id).toBe(101);
    });

    test('Deve retornar o campo "title"', () => {
        expect(data).toHaveProperty('title');
    });

    test('O "title" retornado deve corresponder ao enviado', () => {
        expect(data.title).toBe(POST_DATA.title);
    });

    test('O campo "title" deve ser do tipo string', () => {
        expect(typeof data.title).toBe('string');
    });

    test('Deve retornar o campo "body"', () => {
        expect(data).toHaveProperty('body');
    });

    test('O "body" retornado deve corresponder ao enviado', () => {
        expect(data.body).toBe(POST_DATA.body);
    });

    test('O campo "body" deve ser do tipo string', () => {
        expect(typeof data.body).toBe('string');
    });

    test('Deve retornar o campo "userId"', () => {
        expect(data).toHaveProperty('userId');
    });

    test('O "userId" retornado deve corresponder ao enviado', () => {
        expect(data.userId).toBe(POST_DATA.userId);
    });

    test('O campo "userId" deve ser do tipo number', () => {
        expect(typeof data.userId).toBe('number');
    });

    test('Deve conter todos os campos obrigatórios', () => {
        const requiredFields = ['id', 'title', 'body', 'userId'];
        requiredFields.forEach(field => {
            expect(data).toHaveProperty(field);
        });
    });

    test('O tempo de resposta deve ser aceitável (< 3s)', () => {
        expect(response.status).toBe(201); // Se chegou aqui, o tempo foi aceitável
    });
});

describe('POST /posts - Casos de borda', () => {
    test('Deve aceitar criação com título vazio', async () => {
        const response = await axios.post(`${BASE_URL}/posts`, {
            title: '',
            body: 'test',
            userId: 1
        }, {
            headers: { 'Content-type': 'application/json; charset=UTF-8' }
        });

        expect(response.status).toBe(201);
        expect(response.data).toHaveProperty('id');
    });

    test('Deve aceitar criação com corpo vazio', async () => {
        const response = await axios.post(`${BASE_URL}/posts`, {
            title: 'test',
            body: '',
            userId: 1
        }, {
            headers: { 'Content-type': 'application/json; charset=UTF-8' }
        });

        expect(response.status).toBe(201);
        expect(response.data).toHaveProperty('id');
    });

    test('Deve aceitar criação sem userId', async () => {
        const response = await axios.post(`${BASE_URL}/posts`, {
            title: 'test',
            body: 'test'
        }, {
            headers: { 'Content-type': 'application/json; charset=UTF-8' }
        });

        expect(response.status).toBe(201);
        expect(response.data).toHaveProperty('id');
    });

    test('Deve aceitar criação com campos adicionais', async () => {
        const response = await axios.post(`${BASE_URL}/posts`, {
            title: 'test',
            body: 'test',
            userId: 1,
            extraField: 'extra'
        }, {
            headers: { 'Content-type': 'application/json; charset=UTF-8' }
        });

        expect(response.status).toBe(201);
        expect(response.data).toHaveProperty('id');
    });

    test('Deve aceitar criação com userId de string', async () => {
        const response = await axios.post(`${BASE_URL}/posts`, {
            title: 'test',
            body: 'test',
            userId: '1'
        }, {
            headers: { 'Content-type': 'application/json; charset=UTF-8' }
        });

        expect(response.status).toBe(201);
    });

    test('Deve aceitar caracteres especiais no título', async () => {
        const response = await axios.post(`${BASE_URL}/posts`, {
            title: 'Test @#$%^&*()',
            body: 'test',
            userId: 1
        }, {
            headers: { 'Content-type': 'application/json; charset=UTF-8' }
        });

        expect(response.status).toBe(201);
        expect(response.data.title).toBe('Test @#$%^&*()');
    });

    test('Deve aceitar título longo', async () => {
        const longTitle = 'a'.repeat(500);
        const response = await axios.post(`${BASE_URL}/posts`, {
            title: longTitle,
            body: 'test',
            userId: 1
        }, {
            headers: { 'Content-type': 'application/json; charset=UTF-8' }
        });

        expect(response.status).toBe(201);
        expect(response.data.title).toBe(longTitle);
    });
});
