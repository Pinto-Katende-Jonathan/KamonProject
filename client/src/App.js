import { Route, Routes } from "react-router-dom"
import Dashboard from "./components/Dashboard"
import Articles from "./components/Articles"
import Clients from "./components/Clients"
import Factures from "./components/Creer_Factures"
import PageNotfound from "./components/Notfound"
import NavScroll from "./components/Navb"
import GererFactures from "./components/Gerer_Factures"
import CreerFacture from "./components/Creer_Factures"

function App() {
  return (
    <>
    <NavScroll />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/articles" element={<Articles />} />
        <Route path="/clients" element={<Clients />} />
        <Route path="/factures" element={<Factures />} />
        <Route path="*" element={<PageNotfound />} />
        <Route path="/addInvoice" element={<CreerFacture />} />
        <Route path="/manageInvoice" element={<GererFactures /> } />
      </Routes>
    </>
  );
}

export default App;
