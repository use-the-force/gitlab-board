<script>
    import { priorities } from "../store";

    export let label;

    let text_color = "#ffffff";
    let color = "#777777";
    let name = label;
    
    let use_label = $priorities.filter(p => p.name == label);

    if (use_label) {
        text_color = use_label[0].text_color;
        color = use_label[0].color;
        name = use_label[0].description;
    }
</script>

<span class="badge bg-secondary" style="color: {text_color} !important; background-color: {color} !important;">
    {name}
</span>

<style>
    span.badge {
        font-size: .6rem;
        margin-top: .6rem;
    }
</style>
