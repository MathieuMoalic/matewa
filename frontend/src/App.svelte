<script lang="ts">
	import { Styles } from "sveltestrap";
	import AddWord from "./components/AddWord.svelte";
	import Navbar from "./components/Navbar.svelte";
	import Home from "./components/Home.svelte";
	import Play from "./components/Play.svelte";
	import ListWords from "./components/ListWords.svelte";

	let currentTab = "home";
</script>

<Styles />
<main>
	<Navbar bind:currentTab />
	{#if "home" === currentTab}
		<Home />
	{/if}
	{#if "addWord" === currentTab}
		<AddWord />
	{/if}
	{#if "play" === currentTab}
		<Play />
	{/if}
	{#if "listWords" === currentTab}
		<ListWords />
	{/if}
</main>
