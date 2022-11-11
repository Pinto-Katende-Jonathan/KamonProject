import React from 'react'

const handleDelete = ({id, url}) => {
  const confirm = window.confirm("Etes-vous sûr de supprimer?", id);
  if (confirm) {
    fetch(url + `/${id}`, { method: "DELETE" })
      .then((resp) => resp.json())
      .then((resp) => getUsers());
  }
};

export default handleDelete