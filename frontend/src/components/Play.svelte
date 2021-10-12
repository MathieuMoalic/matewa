<script lang="ts">
    import { onDestroy } from "svelte";
    // import type { WordType } from "../types/word.type";

    import { word, shuffled_word, input_word } from "../store";
    import WordInput from "./Play/WordInput.svelte";
    import Keyboard from "./Play/Keyboard.svelte";
    import CheckInput from "./Play/CheckInput.svelte";
    import { getRandomWord } from "../api/crud";

    async function newWord() {
        $word = await getRandomWord();
    }
    let newWordPromise = newWord();
    onDestroy(() => {
        $word = { en: "", pl: "", fr: "" };
        $input_word = "";
        $shuffled_word = "";
    });
</script>

{#await newWordPromise}
    <p>...waiting</p>
{:then _}
    <WordInput />
    <Keyboard />
    <CheckInput />
{/await}
