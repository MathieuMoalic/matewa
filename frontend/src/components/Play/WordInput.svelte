<script lang="ts">
    import { word, input_word } from "../../store";
</script>

<div class="outer">
    <div class="div1">🇫🇷 {$word.fr}</div>
    <div class="div2">
        🇵🇱 {$input_word}
    </div>
</div>

<style>
    div.outer {
        background-color: var(--c5);
        padding: 2rem;
        border-radius: 2rem;
        border: 2rem solid var(--c1);
    }
</style>
