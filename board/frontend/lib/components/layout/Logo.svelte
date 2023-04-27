<script>
    const getLogoUrl = () => {
        const LOGO_URL = import.meta.env.VITE_LOGO_URL;

        if (!LOGO_URL) {
            return "/images/logo.jpg";
        }

        return LOGO_URL;
    }
</script>

<img src="{getLogoUrl()}" alt="Logo"/>

<style>
    img {
        width: 1.75rem;
        height: auto;
        margin-right: .5rem;
        border-radius: .15rem;
    }
</style>
