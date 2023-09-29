# Função para ler o arquivo .stp e extrair os dados da seção "Graph"
def extract_graph_data(file_path):
    graph_data = []
    reading_graph_section = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Verifique se a seção "Graph" começou
            if line == "Section Graph":
                reading_graph_section = True
                continue
            
            # Verifique se a seção "Graph" terminou
            if line == "Section Terminals":
                break
            
            if reading_graph_section:
                if line.startswith("Nodes"):
                    NumNodes = int(line[6:])
                if line.startswith("Edges"):
                    NumEdges = int(line[6:])
                if line.startswith("E "):
                    parts = line.split()
                    if len(parts) == 4:
                        node1, node2, weight = int(parts[1])-1, int(parts[2])-1, int(parts[3])
                        graph_data.append((node1, node2, weight))
    
    return NumNodes, graph_data, NumEdges

if __name__ == "__main__":    
    # Exemplo de uso
    file_path = 'dmxa0628.stp'
    graph_data = extract_graph_data(file_path)
    print(graph_data)