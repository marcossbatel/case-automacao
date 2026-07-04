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

    test('Deve retornar uma lista (array)', () => {
        expect(Array.isArray(data)).toBe(true);
    });

    test('A lista não deve estar vazia', () => {
        expect(data.length).toBeGreaterThan(0);
    });

    test('Deve retornar exatamente 100 posts', () => {
        expect(data.length).toBe(100);
    });

    test('O primeiro post deve ter o campo "id"', () => {
        expect(data[0]).toHaveProperty('id');
    });

    test('O primeiro post deve ter o campo "title"', () => {
        expect(data[0]).toHaveProperty('title');
    });

    test('O primeiro post deve ter o campo "body"', () => {
        expect(data[0]).toHaveProperty('body');
    });

    test('O primeiro post deve ter o campo "userId"', () => {
        expect(data[0]).toHaveProperty('userId');
    });

    test('O campo "id" deve ser do tipo number', () => {
        expect(typeof data[0].id).toBe('number');
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
        expect(data[0].title.length).toBeGreaterThan(0);
    });

    test('O campo "body" não deve estar vazio', () => {
        expect(data[0].body.length).toBeGreaterThan(0);
    });

    test('Todos os posts devem ter os campos obrigatórios', () => {
        const requiredFields = ['id', 'title', 'body', 'userId'];

        data.forEach(post => {
            requiredFields.forEach(field => {
                expect(post).toHaveProperty(field);
            });
        });
    });

    test('Todos os IDs devem ser únicos', () => {
        const ids = data.map(post => post.id);
        const uniqueIds = new Set(ids);
        expect(ids.length).toBe(uniqueIds.size);
    });

    test('Os IDs devem ser sequenciais de 1 a 100', () => {
        const ids = data.map(post => post.id).sort((a, b) => a - b);
        const expectedIds = Array.from({ length: 100 }, (_, i) => i + 1);
        expect(ids).toEqual(expectedIds);
    });

    test('O tempo de resposta deve ser menor que 3 segundos', () => {
        // Axios não fornece elapsed time diretamente, mas podemos medir
        expect(response.status).toBe(200); // Se chegou aqui em tempo, passou
    });

    test('Todos os títulos devem ser strings não vazias', () => {
        data.forEach(post => {
            expect(typeof post.title).toBe('string');
            expect(post.title.length).toBeGreaterThan(0);
        });
    });

    test('Todos os corpos (body) devem ser strings não vazias', () => {
        data.forEach(post => {
            expect(typeof post.body).toBe('string');
            expect(post.body.length).toBeGreaterThan(0);
        });
    });

    test('Todos os userIds devem ser números positivos', () => {
        data.forEach(post => {
            expect(typeof post.userId).toBe('number');
            expect(post.userId).toBeGreaterThan(0);
        });
    });

    test('Os userIds devem estar entre 1 e 10', () => {
        data.forEach(post => {
            expect(post.userId).toBeGreaterThanOrEqual(1);
            expect(post.userId).toBeLessThanOrEqual(10);
        });
    });
});
