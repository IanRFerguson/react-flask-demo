import './App.css';
import Cowboy from './components/cowboy';
import DisplayMessage from './components/displayMessage';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Cowboy />
        <DisplayMessage />
      </header>
    </div>
  );
}

export default App;
