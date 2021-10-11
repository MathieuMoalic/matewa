<script lang="ts">
    import { onMount } from "svelte";
    import { word } from "../store";
    import WordQuestion from "./WordQuestion.svelte";
    import LetterList from "./LetterList.svelte";
    import { getRandomWord } from "../api/crud";
    onMount(async () => {
        const res = await getRandomWord();
        $word = res;
    });
</script>

<WordQuestion />
<LetterList />
