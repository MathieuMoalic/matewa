import { writable } from 'svelte/store';

export const word = writable({ en: "", pl: "", fr: "" });
export const shuffled_word = writable("shuffled_word");
export const input_word = writable("");