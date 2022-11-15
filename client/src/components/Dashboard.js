import React, {useState, useEffect} from 'react'
import axios from 'axios';

function Dashboard() {
  const [message, setMessage] = useState("")

  
  useEffect(
     () => {
         axios.get("http://localhost:5000/hello")
      .then(res => setMessage(res.data.message))
    }
  ,[])

  return (
    <div>
      <h1 className={{message}?"titre1":""}>{message}</h1>
    </div>
  )
}

export default Dashboard