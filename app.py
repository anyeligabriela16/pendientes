import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calcular_pendiente(x1, y1, x2, y2):
    """
    Calcula la pendiente entre dos puntos
    """
    if x2 - x1 == 0:
        return None  # Pendiente indefinida (línea vertical)
    return (y2 - y1) / (x2 - x1)

def ecuacion_recta(x1, y1, pendiente):
    """
    Calcula la ecuación de la recta en forma y = mx + b
    """
    b = y1 - pendiente * x1
    return pendiente, b

def crear_grafico(x1, y1, x2, y2, pendiente):
    """
    Crea el gráfico mostrando los puntos y la línea
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Puntos
    ax.plot([x1, x2], [y1, y2], 'ro', markersize=8, label='Puntos')
    
    # Línea entre los puntos
    if pendiente is not None:
        # Extender la línea más allá de los puntos
        x_min = min(x1, x2) - 2
        x_max = max(x1, x2) + 2
        x_line = np.linspace(x_min, x_max, 100)
        
        # Calcular y usando la ecuación de la recta
        m, b = ecuacion_recta(x1, y1, pendiente)
        y_line = m * x_line + b
        
        ax.plot(x_line, y_line, 'b-', linewidth=2, label=f'Recta (m = {pendiente:.2f})')
    else:
        # Línea vertical
        y_min = min(y1, y2) - 2
        y_max = max(y1, y2) + 2
        ax.axvline(x=x1, color='b', linewidth=2, label='Línea vertical (pendiente indefinida)')
        ax.set_ylim(y_min, y_max)
    
    # Etiquetas de los puntos
    ax.annotate(f'P1({x1}, {y1})', (x1, y1), xytext=(5, 5), 
                textcoords='offset points', fontsize=10)
    ax.annotate(f'P2({x2}, {y2})', (x2, y2), xytext=(5, 5), 
                textcoords='offset points', fontsize=10)
    
    # Configuración del gráfico
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Gráfico de la Pendiente entre Dos Puntos')
    ax.legend()
    ax.axis('equal')
    
    return fig

def main():
    st.set_page_config(page_title="Calculadora de Pendiente", layout="wide")
    
    st.title("📊 Calculadora de Pendiente entre Dos Puntos")
    st.markdown("---")
    
    # Sidebar para los inputs
    st.sidebar.header("Ingresa las coordenadas de los puntos")
    
    # Punto 1
    st.sidebar.subheader("Punto 1 (P1)")
    x1 = st.sidebar.number_input("Coordenada X1:", value=0.0, step=0.1)
    y1 = st.sidebar.number_input("Coordenada Y1:", value=0.0, step=0.1)
    
    # Punto 2
    st.sidebar.subheader("Punto 2 (P2)")
    x2 = st.sidebar.number_input("Coordenada X2:", value=1.0, step=0.1)
    y2 = st.sidebar.number_input("Coordenada Y2:", value=1.0, step=0.1)
    
    # Opción para mostrar gráfico
    mostrar_grafico = st.sidebar.checkbox("Mostrar gráfico", value=True)
    
    # Calcular pendiente
    pendiente = calcular_pendiente(x1, y1, x2, y2)
    
    # Mostrar resultados
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📋 Resultados")
        
        st.write(f"**Punto 1:** ({x1}, {y1})")
        st.write(f"**Punto 2:** ({x2}, {y2})")
        
        if pendiente is not None:
            st.write(f"**Pendiente (m):** {pendiente:.4f}")
            
            # Calcular ecuación de la recta
            m, b = ecuacion_recta(x1, y1, pendiente)
            
            if b >= 0:
                st.write(f"**Ecuación de la recta:** y = {m:.4f}x + {b:.4f}")
            else:
                st.write(f"**Ecuación de la recta:** y = {m:.4f}x - {abs(b):.4f}")
            
            # Interpretación de la pendiente
            if pendiente > 0:
                st.success("✅ Pendiente positiva: la recta es creciente")
            elif pendiente < 0:
                st.error("❌ Pendiente negativa: la recta es decreciente")
            else:
                st.info("➡️ Pendiente cero: la recta es horizontal")
                
        else:
            st.warning("⚠️ **Pendiente indefinida:** La línea es vertical (x1 = x2)")
        
        # Distancia entre puntos
        distancia = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        st.write(f"**Distancia entre puntos:** {distancia:.4f}")
        
        # Fórmula de la pendiente
        st.subheader("📐 Fórmula utilizada")
        st.latex(r"m = \frac{y_2 - y_1}{x_2 - x_1}")
        
    with col2:
        if mostrar_grafico:
            st.subheader("📈 Gráfico")
            fig = crear_grafico(x1, y1, x2, y2, pendiente)
            st.pyplot(fig)
        else:
            st.info("Activa la opción 'Mostrar gráfico' en la barra lateral para ver la visualización.")
    
    # Información adicional
    st.markdown("---")
    st.subheader("ℹ️ Información")
    st.write("""
    - **Pendiente positiva**: La recta sube de izquierda a derecha
    - **Pendiente negativa**: La recta baja de izquierda a derecha  
    - **Pendiente cero**: La recta es horizontal
    - **Pendiente indefinida**: La recta es vertical (división por cero)
    """)

if __name__ == "__main__":
    main()