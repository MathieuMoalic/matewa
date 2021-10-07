<script lang="ts">
    import { Nav, NavItem, NavLink } from "sveltestrap";

    export let currentTab = "listWords";
</script>

<Nav tabs>
    <NavItem>
        <NavLink
            on:click={() => (currentTab = "home")}
            class={currentTab === "home" ? "active" : ""}>Home</NavLink
        >
    </NavItem>
    <NavItem>
        <NavLink
            on:click={() => (currentTab = "play")}
            class={currentTab === "play" ? "active" : ""}>Play</NavLink
        >
    </NavItem>
    <NavItem>
        <NavLink
            on:click={() => (currentTab = "addWord")}
            class={currentTab === "addWord" ? "active" : ""}>Add Word</NavLink
        >
    </NavItem>
    <NavItem>
        <NavLink
            on:click={() => (currentTab = "listWords")}
            class={currentTab === "listWords" ? "active" : ""}>Words</NavLink
        >
    </NavItem>
</Nav>
