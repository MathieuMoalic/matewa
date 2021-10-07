<script lang="ts">
    import { onMount } from "svelte";

    import { Icon, Col, Container, Row } from "sveltestrap";

    import { getWordList } from "../api/crud";
    import UpdateWord from "./UpdateWord.svelte";

    let words = [];
    onMount(async () => {
        const res = await getWordList();
        words = res;
    });
</script>

<main>
    <Container>
        {#each words as word}
            <Row>
                <Col>🇬🇧 {word.en}</Col>
                <Col>🇫🇷 {word.fr}</Col>
                <Col>🇵🇱 {word.pl}</Col>
                <Col xs="1"><Icon name="wrench" /></Col>
            </Row>
        {/each}
    </Container>
</main>
