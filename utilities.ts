import * as fs from "fs";
const fsPromises = fs.promises;

// Read file, returns a string of the whole file
export const readFile = async (file: string): Promise<string> =>
    (await fsPromises.readFile(file, 'utf8')).toString()

// Read file, returns a list of lines
export const readFileLines = async (file: string): Promise<string[]> =>
    (await fsPromises.readFile(file, 'utf8')).toString().split('\r\n')

// Read file, returns a list of paragraphs (seperated by newlines)
export const readFileParagraphs = async (file: string): Promise<string[]> =>
    (await fsPromises.readFile(file, 'utf8')).toString().split('\r\n\r\n')
