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

<div>
    <span class="badge bg-secondary" style="color: {text_color} !important; background-color: {color} !important;">
        {name}
    </span>
</div>

<style>
    span.badge {
        font-size: .6rem;
        margin-top: .6rem;
    }
</style>
