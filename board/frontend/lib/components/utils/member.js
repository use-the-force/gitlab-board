export const getMemberAvatar = (member) => {
    if (member && member.avatar_url) {
        return member.avatar_url;
    }

    return "/images/no-avatar.jpg";
}