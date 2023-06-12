<script>
    import {Router, Route} from "svelte-navigator";
    import Home from "./lib/components/pages/Home.svelte";
    import Login from "./lib/components/pages/Login.svelte";
    import {beforeUpdate} from "svelte";
    import {authRequired} from "./lib/api/auth.js";

    // TODO: do before rendering
    beforeUpdate(() => {
        authRequired();
    })
</script>


<Router>
    <Route path={`${global.BOARD_SUBPATH}/`}>
        <Home/>
    </Route>
    <Route path={`${global.BOARD_SUBPATH}/login`}>
        <Login/>
    </Route>
</Router>

<style>

</style>
