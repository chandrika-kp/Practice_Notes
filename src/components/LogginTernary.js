import React from 'react'
let element = null;
let isLoggedIn = false;
  

 function LogginTernary() {
  return (
    <div>
      isLoggedIn
    ? (element = <h2>Welcome Admin</h2>)
    : (element = <h2>Please Login</h2>);
      
    </div>
  )
}
export default LogginTernary()
