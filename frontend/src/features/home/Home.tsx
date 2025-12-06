import Header from '../../components/layout/Header';

function Home() {
    return (
        <div className="min-h-screen bg-gray-50">
            <Header />
            
            <main className="p-6">
                <h2 className="text-2xl font-bold">Welcome to Signalytic</h2>
                <p className="mt-2 text-gray-600">
                    This is your main page. Start building features here.
                </p>
            </main>
        </div>
    );
}

export default Home;