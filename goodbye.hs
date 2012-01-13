import Network
import System.IO

main = do
  sock <- listenOn (PortNumber 7778)
  (h, host, port) <- accept sock
  var <- hGetLine h
  putStrLn "[6] Goodbye, world"
