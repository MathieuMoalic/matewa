<script lang="ts">
    import { postWord } from "../api/crud";
    let word = {
        pl: "",
        en: "",
        fr: "",
    };
    let addWord = async () => {
        await postWord(word);
    };
</script>

<main>
    <input bind:value={word.en} placeholder="Word in English" />
    <input bind:value={word.pl} placeholder="Word in Polish" />
    <input bind:value={word.fr} placeholder="Word in French" />
    <button
        type="submit"
        on:click|preventDefault={addWord}
        class="btn btn-primary">Add Word</button
    >
</main>
