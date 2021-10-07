<script lang="ts">
    import {
        Button,
        Modal,
        ModalBody,
        ModalFooter,
        ModalHeader,
        Icon,
    } from "sveltestrap";
    import { updateWord } from "../api/crud";
    export let word = { en: "", fr: "", pl: "", id: 0 };
    let updatedWord = { en: "", fr: "", pl: "" };
    let open = false;
    const toggle = () => (open = !open);
    let onUpdateWordButton = async () => {
        await updateWord(word.id, updatedWord);
        toggle();
    };
</script>

<div>
    <Button size="sm" outline color="warning" on:click={toggle}
        ><Icon name="wrench" /></Button
    >
    <Modal isOpen={open} {toggle}>
        <ModalHeader {toggle}>Modify a word</ModalHeader>
        <ModalBody>
            <input bind:value={updatedWord.en} placeholder="🇬🇧 {word.en}" />
            <input bind:value={updatedWord.pl} placeholder="🇫🇷 {word.fr}" />
            <input bind:value={updatedWord.fr} placeholder="🇵🇱 {word.pl}" />
        </ModalBody>
        <ModalFooter>
            <Button color="primary" on:click={onUpdateWordButton}
                >Modify the word</Button
            >
            <Button color="secondary" on:click={toggle}>Cancel</Button>
        </ModalFooter>
    </Modal>
</div>
