import apis from './apis';

jest.mock('axios'); // This overwrites axios methods with jest Mock
import axios from 'axios';

describe('Test Apis', () => {
    describe('getResource', () => {
        describe('with success', () => {
            const url = 'http://127.0.0.1:8000/';
            const onComplete = jest.fn();
            const data = {};

            beforeEach(() => {
                axios.get.mockResolvedValue(data);
            });

            it('should call axios get with given url', () => {
                getResource(url, onComplete);
                expect(axios.get).toBeCalledWith(url);
            });

            it('should call onComplete callback with response', async () => { // do not forget 'async'
                await getResource(url, onComplete); // notice the 'await' because onComplete callback is called in '.then'
                expect(onComplete).toBeCalledWith(data);
            });
        });
    });
});