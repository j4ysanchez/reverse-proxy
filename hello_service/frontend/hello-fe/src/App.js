import logo from './logo.svg';
import './App.css';

import UserTable from './UserTable';
import WorldComponent from './WorldComponent';

function App() {
  return (
    <div className="App">
      <h1>AP Request</h1>
      <WorldComponent />
      <h1>User Table</h1>
      <UserTable />
    </div>
  );
}

export default App;
