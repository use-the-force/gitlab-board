<script>
    import {
        Container,
        Styles
    } from "sveltestrap";
    import Navbar from "../layout/Navbar.svelte";
    import Footer from "../layout/Footer.svelte";
    import {settingsMergeRequests} from "../../store.js";

    const handleChangeSettingGeneralMergeRequests = async (e) => {
        $settingsMergeRequests = e.target.checked;
    }
</script>

<Styles/>

<Navbar></Navbar>

<Container fluid class="py-4 bg-white">
    <div class="col-12 col-lg-10 col-xl-8 mx-auto">
        <h2 class="h3 mb-4 page-title">Settings</h2>
        <div class="my-4">
            <ul class="nav nav-tabs mb-4" id="myTab" role="tablist">
                <li class="nav-item">
                    <a class="nav-link active" id="contact-tab" data-toggle="tab" href="#contact" role="tab" aria-controls="contact"
                       aria-selected="false">General</a>
                </li>
            </ul>
            <h5 class="mb-0 mt-5">Feature Settings</h5>
            <p>Select features you want to enable.</p>
            <div class="list-group mb-5">
                <div class="list-group-item">
                    <div class="row align-items-center">
                        <div class="col">
                            <strong class="mb-0">Merge Requests</strong>
                            <p class="text-muted mb-0">Include merge requests in kanban desk.</p>
                        </div>
                        <div class="col-auto">
                            <input
                                    type="checkbox"
                                    checked={$settingsMergeRequests == "true"}
                                    on:change={handleChangeSettingGeneralMergeRequests}/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</Container>

<Footer></Footer>

<style>
    h2:focus-visible {
        outline: none;
    }

    input[type=checkbox] {
        width: 2rem;
        height: 2rem;
    }
</style>
