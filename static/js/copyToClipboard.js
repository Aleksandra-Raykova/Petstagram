function copyToClipboard(photo_id) {
  const host = window.location.hostname;
  navigator.clipboard.writeText(host + `/share/${photo_id}`);
}