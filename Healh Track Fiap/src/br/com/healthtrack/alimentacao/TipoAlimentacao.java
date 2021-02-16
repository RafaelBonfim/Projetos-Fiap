package br.com.healthtrack.alimentacao;

/**
 * 
 * Define o tipo de refei��o que foi feita, automaticamente atribu�do conforme
 * a constru��o do objeto Alimentacao
 *
 */

public class TipoAlimentacao {
	private byte codAlim;
	private String descAlim;
	
	public byte getCodAlim() {
		return codAlim;
	}
	public void setCodAlim(byte codAlim) {
		this.codAlim = codAlim;
	}
	public String getDescAlim() {
		return descAlim;
	}
	public void setDescAlim(String descAlim) {
		this.descAlim = descAlim;
	}
	
}
