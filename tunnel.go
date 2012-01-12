package main

import (
    "fmt"
    "net"
    "os"
    "time"
)

func exit_on_error(err os.Error) {
    if err != nil {
        fmt.Print(err.String() + "\n")
        os.Exit(1)
    }
}

/* Create a pipe within the two connections */
func tcp_sock_pipe (in, out net.Conn) os.Error {
    var b [1024]byte
    var err os.Error
    var n int

    for ; err == nil; n, err = in.Read(b[0:]) {
        out.Write(b[0:n])
    }
    return err
}

func main() {
    listen_ip, err := net.ResolveTCPAddr("tcp", "127.0.0.1:7777")
    connect_ip, err := net.ResolveTCPAddr("tcp", "127.0.0.1:7778")

    // Create both server and client sockets
    listen_socket, err := net.ListenTCP("tcp", listen_ip)
    exit_on_error(err)

    out_conn, err := net.DialTCP("tcp", nil, connect_ip)
    exit_on_error(err)

    // Exit when socket server if on EOF 
    in_conn, err  := listen_socket.AcceptTCP()
    exit_on_error(err)

    in_conn.SetReadTimeout(0)

    time.Sleep(1e9)
    fmt.Print("[5] Tunnel up and running\n")
    tcp_sock_pipe(in_conn, out_conn)
}
