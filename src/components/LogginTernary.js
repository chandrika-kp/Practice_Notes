import React from 'react'
let element = null;
let isLoggedIn = false;

// Using if-else:

// function App() {
//   let element = null;
//   let isLoggedIn = false;
//   if (isLoggedIn) {
//     element = <h2>Welcome Admin</h2>;
//   } else {
//     element = <h2>Please Login</h2>;
//   }
//   return <>{element}</>;
// }
// export default App;


// 2. Using ternary operator:

// function App() {
//   let isLoggedIn = false;
//   return isLoggedIn ? <h2>Welcome Admin</h2> : <h2>Please Login</h2>;
// }
// export default App;

// 3. Using variables:

function LogginTernary() {
  isLoggedIn
    ? (element = <h2>Welcome Admin</h2>)
    : (element = <h2>Please Login</h2>);
  return (
    <div>
      {element} 
    </div>
  )
}
export default LogginTernary
