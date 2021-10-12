<script lang="ts">
    import { onDestroy } from "svelte";
    // import type { WordType } from "../types/word.type";

    import { word, shuffled_word, input_word } from "../store";
    import WordInput from "./WordInput.svelte";
    import LetterList from "./LetterList.svelte";
    import CheckInput from "./CheckInput.svelte";
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
    <LetterList />
    <CheckInput />
{/await}
