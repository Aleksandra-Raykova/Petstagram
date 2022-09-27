function copyToClipboard(photo_id) {
  const host = window.location.hostname;
  navigator.clipboard.writeText(host + `/photo/${photo_id}`);
}