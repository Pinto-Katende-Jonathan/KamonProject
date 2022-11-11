import React, { useState, useEffect } from "react";
import "../App.css";
import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import FormDialog from "./dialogClient";

import ButtonsEditDel from "./ButtonsEditDel";

const initialValue = { name: "", phone: "" };
function Client() {
  const [gridApi, setGridApi] = useState(null);
  const [tableData, setTableData] = useState(null);
  const [open, setOpen] = React.useState(false);
  const [formData, setFormData] = useState(initialValue);
  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
    setFormData(initialValue);
  };
  const url = `http://localhost:5000/client`;
  const columnDefs = [
    { headerName: "ID", field: "id" },
    { headerName: "Nom", field: "name" },
    { headerName: "Phone", field: "phone" },
    {
      headerName: "Actions",
      field: "id",
      cellRendererFramework: (params) => (
        <ButtonsEditDel
          params={params}
          handleUpdate={handleUpdate}
          handleDelete={handleDelete}
        />
      ),
    },
  ];
  // calling getUsers function for first time
  useEffect(() => {
    getUsers();
  }, []);

  //fetching users data from server
  const getUsers = () => {
    fetch(url + "s")
      .then((resp) => resp.json())
      .then((resp) => setTableData(resp));
  };
  const onChange = (e) => {
    const { value, id } = e.target;
    // console.log(value,id)
    setFormData({ ...formData, [id]: value });
  };
  const onGridReady = (params) => {
    setGridApi(params);
  };

  // setting update row data to form data and opening pop up window
  const handleUpdate = (oldData) => {
    setFormData(oldData);
    handleClickOpen();
  };
  //deleting a user
  const handleDelete = (id) => {
    const confirm = window.confirm("Etes-vous sûr de supprimer?", id);
    if (confirm) {
      fetch(url + `/${id}`, { method: "DELETE" })
        .then((resp) => resp.json())
        .then((resp) => getUsers());
    }
  };
  const handleFormSubmit = () => {
    if (formData.id) {
      //updating a user
      if (formData.name.trim() !== "" && formData.phone.trim() !== "") {
        fetch(url + `/${formData.id}`, {
          method: "PUT",
          body: JSON.stringify({
            name: formData.name,
            phone: formData.phone,
          }),
          headers: {
            "content-type": "application/json",
          },
        })
          .then((resp) => resp.json())
          .then((resp) => {
            handleClose();
            getUsers();
          });
      }
    } else {
      // adding new user
      if (formData.name.trim() !== "" && formData.phone.trim() !== "") {
        fetch(url, {
          method: "POST",
          body: JSON.stringify(formData),
          headers: {
            "content-type": "application/json",
          },
        })
          .then((resp) => resp.json())
          .then((resp) => {
            handleClose();
            getUsers();
          });
      }
    }
  };

  const defaultColDef = {
    sortable: true,
    flex: 1,
    filter: true,
    floatingFilter: true,
  };
  return (
    <div className="Client">
      <h1 className="titre1" align="center">Client</h1>
      <Grid align="right">
        <Button
          style={{ margin: 20, width: "40%" }}
          variant="contained"
          color="primary"
          onClick={handleClickOpen}
        >
          Ajouter un client
        </Button>
      </Grid>
      <div className="ag-theme-alpine" style={{ height: "400px", padding: 20 }}>
        <AgGridReact
          rowData={tableData}
          columnDefs={columnDefs}
          defaultColDef={defaultColDef}
          onGridReady={onGridReady}
        />
      </div>
      <FormDialog
        open={open}
        handleClose={handleClose}
        data={formData}
        onChange={onChange}
        handleFormSubmit={handleFormSubmit}
      />
    </div>
  );
}

export default Client;
