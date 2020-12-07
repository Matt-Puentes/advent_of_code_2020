import * as util from '../utilities'

const questions = 'abcdefghijklmnopqrstuvwxyz'.split('')

const part1 = (input: string[]) => input.reduce(
    (accumulator: number, group: string) => accumulator + group.split('').reduce((accumulator, char) => accumulator + (questions.includes(char) && !(accumulator.includes(char)) ? char : '')).length, 0);
    

const part2 = (input: string[]) => input.reduce(
    (accumulator: number, group: string) => accumulator + 
        questions.map( (char: string) => (group.match(new RegExp(`${char}`, 'g')) || []).length ).reduce(
            (a: number, e: number) => a + (e == group.trim().split('\r\n').length ? 1 : 0)
        , 0)
    , 0);

(async () => {
    const input = await util.readFileParagraphs('input');
    console.log(input)
    console.log("Part 1: " + part1(input));
    console.log("Part 2: " + part2(input));
})();
