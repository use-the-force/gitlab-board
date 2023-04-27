<script>
    import { defaultType, types } from "../../store.js";

    export let labels;

    export function getTypeColor() {
        let type;
        let label = labels.find(label => {
            if (label.includes("Type::")) {
                return label;
            }
        });
        type = $types.find(type => {
            if (type.name === label) {
                return type;
            }
        });

        if (type) {
            return type.color;
        }

        return $defaultType.color;
    }
</script>

<span class="dot" style="background: {getTypeColor()}"></span>

<style>
    .dot {
        height: .65rem;
        width: .65rem;
        border-radius: .15rem;
        display: inline-block;
    }
</style>
