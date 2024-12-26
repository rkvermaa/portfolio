import Navbar from './components/Navbar'
import Hero from './components/Hero'
import './App.css'

function App() {
  return (
    <>
      <Navbar />
      <div className="content">
        <Hero />
      </div>
    </>
  )
}

export default App