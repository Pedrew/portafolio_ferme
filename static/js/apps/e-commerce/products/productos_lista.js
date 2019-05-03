(function () {
    $(document).ready(function () {
        $('.dataTable').DataTable(
            {
                dom       : 'rt<"dataTables_footer"ip>',
                initComplete  : function () {
                    var api = this.api(),
                        searchBox = $('#products-search-input');

                    // Bind an external input as a table wide search box
                    if ( searchBox.length > 0 )
                    {
                        searchBox.on('keyup', function (event) {
                            api.search(event.target.value).draw();
                        });
                    }
                },
                lengthMenu    : [10, 20, 30, 50, 100],
                pageLength    : 10,
                language      : {
                                    "sProcessing":     "Procesando...",
                                    "sLengthMenu":     "Mostrar _MENU_ registros",
                                    "sZeroRecords":    "No se encontraron resultados",
                                    "sEmptyTable":     "Ningún dato disponible en esta tabla",
                                    "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
                                    "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
                                    "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
                                    "sInfoPostFix":    "",
                                    "sSearch":         "Buscar:",
                                    "sUrl":            "",
                                    "sInfoThousands":  ",",
                                    "sLoadingRecords": "Cargando...",
                                    "oPaginate": {
                                        "sFirst":    "Primero",
                                        "sLast":     "Último",
                                        "sNext":     "Siguiente",
                                        "sPrevious": "Anterior"
                                    },
                                    "oAria": {
                                        "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                                        "sSortDescending": ": Activar para ordenar la columna de manera descendente"
                                    }
                                },
                scrollY       : 'auto',
                scrollX       : false,
                responsive    : true,
                autoWidth     : false,
                scrollCollapse: true
            }
        );

    });
})();