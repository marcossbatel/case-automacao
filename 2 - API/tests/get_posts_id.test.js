import { describe, test, expect, beforeAll } from 'vitest';
import axios from 'axios';

const BASE_URL = 'https://jsonplaceholder.typicode.com';
const USER_ID = 1;

let response;
let data;

describe('GET /posts/1 - Buscar post com id 1', () => {
    beforeAll(async () => {
        response = await axios.get(`${BASE_URL}/posts/1`);
        data = response.data;
    });

    test('O status do retorno deve ser 200', () => {
        expect(response.status).toBe(200);
    });

    test('A resposta é um objeto JSON', () => {
        expect(typeof data).toBe('object');
    });

    test('O ID do retorno é igual a 1', () => {
        expect(data.id).toBe(1);
    });

    test('O retorno possui todos os campos e nenhum é vazio', () => {
        const camposObrigatorios = ['id', 'title', 'body', 'userId'];
        camposObrigatorios.forEach(field => {
            expect(data).toHaveProperty(field);
        });
        expect(data.id).not.toBeNull();
        expect(data.title).to.not.be.empty;
        expect(data.body).to.not.be.empty;
        expect(data.userId).not.toBeNull();
    });

    test('O tipo de cada campo no retorno é correto', () => {
        expect(typeof data.id).toBe('number');
        expect(typeof data.title).toBe('string');
        expect(typeof data.body).toBe('string');
        expect(typeof data.userId).toBe('number');
    });

    test('O body do retorno não é vazio', () => {
        expect(data.body.length).toBeGreaterThan(0);
    });
});

describe('GET /posts/1 - Buscar post com id inexistente', () => {
    beforeAll(async () => {
        response = await axios.get(`${BASE_URL}/posts/9999`, {
            validateStatus: () => true
        });
    });

    test('O status do retorno é 404', () => {
        expect(response.status).toBe(404);
    });

    test('O retorno é vazio', async () => {
        expect(response.data).toEqual({});
    });
});
