<script>
    import { labels } from "../../store";

    export let label;

    let text_color = "#ffffff";
    let color = "#777777";
    let name = label;

    if ($labels[label]) {
        text_color = $labels[label].text_color;
        color = $labels[label].color;
        name = $labels[label].description;
    }
</script>

<span class="badge bg-secondary rounded-pill" style="color: {text_color} !important; background-color: {color} !important;">
    {name}
</span>

<style>
    span.badge {
        font-size: .6rem;
        margin-top: 1rem;
        margin-right: 0.5em;
    }
</style>
