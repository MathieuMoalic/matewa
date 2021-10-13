<script lang="ts">
    import { postWord } from "../api/crud";
    import { Icon } from "sveltestrap";
    export let currentPage: string;
    let input_word = {
        pl: "",
        en: "",
        fr: "",
    };
    let addWord = async () => {
        await postWord(input_word);
        input_word = {
            pl: "",
            en: "",
            fr: "",
        };
    };
    function backHome() {
        currentPage = "home";
    }
</script>

<main>
    <input bind:value={input_word.en} placeholder="🇬🇧" />
    <input bind:value={input_word.pl} placeholder="🇵🇱" />
    <input bind:value={input_word.fr} placeholder="🇫🇷" />
    <button class="default" type="submit" on:click|preventDefault={addWord}
        >Add Word</button
    >
    <button class="default" type="submit" on:click|preventDefault={backHome}
        ><Icon name="arrow-return-left" /></button
    >
</main>

<style>
    input {
        width: 75%;
        margin: 1rem;
        border-width: 2px;
        border-color: var(--c2);
        border-radius: 1rem;
    }
</style>
