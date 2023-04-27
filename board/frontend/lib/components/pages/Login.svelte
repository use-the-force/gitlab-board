<script>
    import Cookies from "js-cookie";

    import { Styles } from "sveltestrap";
    import { beforeUpdate } from "svelte";
    import { authorized } from "../../store.js";
    import Navbar from "../layout/Navbar.svelte";
    import { login } from "../../api/board.js";
    import { isAuthorized } from "../../api/auth.js";
    import Footer from "../layout/Footer.svelte";

    const submitForm = async (e) => {
        const formData = new FormData(e.target)

        // TODO: Add proper validation
        let username = formData.get("username");
        let password = formData.get("password");

        if (!username || !password) {
            alert("Please fill username and password");
        }

        await login(username, password);
        $authorized = Cookies.get("authorized");
        window.location.pathname = "/";
    };

    // TODO: do before rendering
    beforeUpdate(() => {
        if (isAuthorized()) {
            window.location.pathname = "/";
        }
    })
</script>

<Styles/>

<Navbar></Navbar>

<section class="bg-white py-4">
    <div class="px-4 py-5 px-md-5 text-center text-lg-start">
        <div class="container">
            <div class="row gx-lg-5 align-items-center">
                <div class="col-lg-6 mb-5 mb-lg-0">
                    <h1 class="my-5 display-3 fw-bold ls-tight">
                        GitLab Board <br/>
                        <span class="text-primary">Extended board for Community Edition</span>
                    </h1>
                </div>

                <div class="offset-md-1 col-lg-5 mb-5 mb-lg-0">
                    <div class="card">
                        <div class="card-body py-5 px-md-5">
                        <h5 class="text-center mb-4">Login to continue the work</h5>
                            <form on:submit|preventDefault={submitForm}>
                                <div class="form-outline mb-4">
                                    <input type="text" id="username" name="username" class="form-control" placeholder="Username" required/>
                                </div>
                                <div class="form-outline mb-4">
                                    <input type="password" id="password" name="password" class="form-control" placeholder="Password" required/>
                                </div>
                                <button type="submit" class="btn btn-primary btn-block mb-4 w-100">
                                    Sign in
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<Footer></Footer>

<style>
    input, button {
        height: 2.75rem;
    }

    h1:focus-visible {
        outline: none;
    }
</style>
