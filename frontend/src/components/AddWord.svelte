<script lang="ts">
    let word = {
        pl: "",
        en: "",
        fr: "",
    };
    let addWord = () => {
        const request = new Request("http://localhost:8000/word/", {
            method: "POST",
            body: JSON.stringify(word),
            headers: new Headers({
                "Content-Type": "application/json",
            }),
        });

        // pass request object to `fetch()`
        fetch(request)
            .then((res) => res.json())
            .then((res) => console.log(res));
    };
</script>

<main>
    <input bind:value={word.en} placeholder="word_en" />
    <input bind:value={word.pl} placeholder="word_pl" />
    <input bind:value={word.fr} placeholder="word_fr" />
    <button
        type="submit"
        on:click|preventDefault={addWord}
        class="btn btn-primary">Add Word</button
    >
</main>
