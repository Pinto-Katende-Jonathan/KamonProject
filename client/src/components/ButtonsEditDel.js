import React from "react";
import Button from "@mui/material/Button";

function ButtonsEditDel({params, handleUpdate, handleDelete}) {
  return (
    <div>
      <Button
        variant="outlined"
        color="primary"
        onClick={() => handleUpdate(params.data)}
        style={{ margin: 3, height: 30 }}
      >
        Update
      </Button>
      <Button
        style={{ margin: 3, height: 30 }}
        variant="contained"
        color="error"
        onClick={() => handleDelete(params.value)}
      >
        Delete
      </Button>
    </div>
  );
}

export default ButtonsEditDel;
