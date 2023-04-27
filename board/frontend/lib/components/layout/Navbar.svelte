<script>
    import {
        Nav,
        Dropdown,
        DropdownToggle,
        DropdownMenu,
        DropdownItem
    } from "sveltestrap";
    import Logo from "./Logo.svelte";
    import { isAuthorized, logout } from "../../api/auth.js";
    import UserAvatar from "../UserAvatar.svelte";
</script>


<nav id="navbar" class="navbar navbar-expand-md navbar-light bg-light border-bottom">
    <div class="container-fluid">
        <Logo></Logo>
        <a class="me-auto navbar-brand" href="/">GitLab Board</a>

        {#if isAuthorized()}
            <Nav class="ms-auto" navbar>
                <Dropdown nav inNavbar>
                    <DropdownToggle class="custom-dropdown-toggle" nav caret>
                        <UserAvatar></UserAvatar>
                    </DropdownToggle>
                    <DropdownMenu end>
                        <DropdownItem divider/>
                        <DropdownItem on:click={(e) => logout()}>
                            Logout
                        </DropdownItem>
                    </DropdownMenu>
                </Dropdown>
            </Nav>
        {/if}
    </div>
</nav>


<style>
    .navbar {
        height: 3.75rem;
    }

    .navbar-brand {
        font-size: 1rem;
    }

    .custom-dropdown-toggle::after {
        display: none !important;
        background: red;
    }
</style>

